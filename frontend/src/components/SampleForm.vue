<template>
  <v-card
    class="mb-6"
    outlined
  >
    <v-card-title>Adicionar Nova Amostra</v-card-title>
    <v-card-text>
      <v-form
        @submit.prevent="submitSample"
        ref="form"
      >
        <v-row dense>
          <v-col
            cols="12"
            sm="6"
            md="4"
            v-for="field in fields"
            :key="field.name"
          >
            <v-text-field
              v-model="sample[field.name]"
              :label="field.label"
              :type="'number'"
              :rules="[(v) => !!v || 'Campo obrigatório']"
              required
              density="compact"
              step="any"
            />
          </v-col>
        </v-row>
        <v-btn
          color="primary"
          type="submit"
          >Salvar Amostra</v-btn
        >
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script setup>
import { reactive, ref } from "vue";
import { addSample } from "@/service/sampleService";

const emit = defineEmits(["submitted"]);

const sample = reactive({
  ph: null,
  nitrogen: null,
  phosphorus: null,
  potassium: null,
  compaction: null,
});

const fields = [
  { name: "ph", label: "pH" },
  { name: "nitrogen", label: "Nitrogênio (ppm)" },
  { name: "phosphorus", label: "Fósforo (ppm)" },
  { name: "potassium", label: "Potássio (ppm)" },
  { name: "compaction", label: "Compactação (g/cm³)" },
];

const form = ref(null);

const submitSample = async () => {
  const isValid = await form.value.validate();
  if (!isValid.valid) return;

  // Converter os valores para números antes de enviar
  const formattedSample = Object.fromEntries(
    Object.entries(sample).map(([key, value]) => [key, parseFloat(value)])
  );

  await addSample(formattedSample);
  Object.keys(sample).forEach((k) => (sample[k] = null));
  emit("submitted");
};
</script>
