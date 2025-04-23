<template>
  <v-card outlined>
    <v-card-title>Distribuição Média dos Parâmetros</v-card-title>
    <v-card-text>
      <canvas  ref="chartCanvas"></canvas>
    </v-card-text>
  </v-card>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

const props = defineProps({
  samples: {
    type: Array,
    required: true,
  },
});

const chartCanvas = ref(null);
let chartInstance = null;

function mountChart() {
  const averages = {
    ph: 0,
    nitrogen: 0,
    phosphorus: 0,
    potassium: 0,
    compaction: 0,
  };

  props.samples.forEach((sample) => {
    averages.ph += sample.ph;
    averages.nitrogen += sample.nitrogen;
    averages.phosphorus += sample.phosphorus;
    averages.potassium += sample.potassium;
    averages.compaction += sample.compaction;
  });

  const sampleCount = props.samples.length;
  Object.keys(averages).forEach((key) => {
    averages[key] = (averages[key] / sampleCount).toFixed(2);
  });

  const data = {
    labels: ["pH", "Nitrogênio", "Fósforo", "Potássio", "Compactação"],
    datasets: [
      {
        label: "Média dos Parâmetros",
        data: Object.values(averages),
        backgroundColor: ["#4CAF50", "#2196F3", "#FFC107", "#FF5722", "#9C27B0"],
      },
    ],
  };

  if (chartInstance) chartInstance.destroy();

  chartInstance = new Chart(chartCanvas.value, {
    type: "bar",
    data,
    options: {
      responsive: true,
      plugins: {
        legend: {
          display: false,
        },
      },
    },
  });
}

watch(() => props.samples, mountChart, { deep: true });
onMounted(mountChart);
</script>