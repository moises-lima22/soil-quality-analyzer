<template>
  <v-card class="mb-6" outlined>
    <v-card-title>Amostras Registradas</v-card-title>
    <v-data-table
      :headers="headers"
      :items="samples"
      class="elevation-1"
      dense
      disable-sort
    >
      <template #item.index="{ index }">
        {{ index + 1 }}
      </template>
    </v-data-table>
  </v-card>
</template>

<script setup>
defineProps({
  samples: {
    type: Array,
    required: true
  }
})

const headers = [
  { text: '#', value: 'index' },
  { text: 'pH', value: 'ph' },
  { text: 'Nitrogênio (ppm)', value: 'nitrogen' },
  { text: 'Fósforo (ppm)', value: 'phosphorus' },
  { text: 'Potássio (ppm)', value: 'potassium' },
  { text: 'Compactação (g/cm³)', value: 'compaction' }
]
</script>
