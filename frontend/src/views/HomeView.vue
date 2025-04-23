<template>
  <v-container>
    <h1 class="text-h5 mb-4">Soil Quality Analyzer 🌱</h1>
    <SampleTable
      :samples="samples"
      @add="handleAdd"
      @edit="handleEdit"
      @delete="handleDelete"
    />
    <v-row class="mt-4">
      <v-col cols="4">
        <v-card outlined>
          <EvaluationChart :results="evaluations" />
        </v-card>
      </v-col>
      <v-col cols="8">
        <v-card outlined>
          <ParameterDistributionChart :samples="samples" />
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import {
  fetchSamples,
  evaluateSamples,
  addSample,
  updateSample,
  deleteSample,
} from "@/service/sampleService";
import SampleTable from "@/components/SampleTable.vue";
import EvaluationChart from "@/components/EvaluationChart.vue";
import ParameterDistributionChart from "@/components/ParameterDistributionChart.vue";

const samples = ref([]);
const evaluations = ref([]);

async function loadSamples() {
  samples.value = await fetchSamples();
  evaluations.value = await evaluateSamples();
}

async function handleAdd(newSample) {
  await addSample(newSample);
  loadSamples(); // Recarrega os dados após adicionar
}

async function handleEdit(updatedSample) {
  await updateSample(updatedSample.id, updatedSample);
  loadSamples(); // Recarrega os dados após editar
}

async function handleDelete(id) {
  await deleteSample(id);
  loadSamples(); // Recarrega os dados após excluir
}

onMounted(loadSamples);
</script>

<style scoped></style>
