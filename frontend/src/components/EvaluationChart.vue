<template>
  <v-card outlined>
    <v-card-title>Distribuição de Qualidade do Solo</v-card-title>
    <v-card-text class="chart-container">
      <canvas ref="chartCanvas"></canvas>
    </v-card-text>
  </v-card>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

const props = defineProps({
  results: {
    type: Array,
    required: true,
  },
});

const chartCanvas = ref(null);
let chartInstance = null;

function mountChart() {
  const apto = props.results.filter((r) => r.status === "Apto").length;
  const inapto = props.results.filter((r) => r.status === "Inapto").length;

  const data = {
    labels: ["Apto", "Inapto"],
    datasets: [
      {
        data: [apto, inapto],
        backgroundColor: ["#4CAF50", "#F44336"],
      },
    ],
  };

  if (chartInstance) chartInstance.destroy();

  chartInstance = new Chart(chartCanvas.value, {
    type: "doughnut",
    data,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: "bottom",
        },
      },
    },
  });
}

watch(() => props.results, mountChart, { deep: true });
onMounted(mountChart);
</script>

<style scoped>
.chart-container {
  position: relative;
  height: 100%; /* Garante que o canvas ocupe toda a altura disponível */
}

canvas {
  width: 100% !important; /* O canvas ocupa toda a largura */
  height: 100% !important; /* O canvas ocupa toda a altura */
}
</style>
