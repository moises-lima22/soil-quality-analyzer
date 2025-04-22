<template>
  <v-container>
    <h1 class="text-h5 mb-4">Soil Quality Analyzer 🌱</h1>
    <SampleForm @submitted="fetchSamples" />
    <SampleTable :samples="samples" />
    <EvaluationChart :results="evaluations" />
  </v-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { fetchSamples, evaluateSamples } from "@/service/sampleService";
import SampleForm from "@/components/SampleForm.vue";
import SampleTable from "@/components/SampleTable.vue";
import EvaluationChart from "@/components/EvaluationChart.vue";

const samples = ref([]);
const evaluations = ref([]);

async function loadSamples() {
  samples.value = await fetchSamples();
  evaluations.value = await evaluateSamples();
}

onMounted(loadSamples);
</script>
