<template>
  <v-card
    class="mb-6 px-6 py-8"
    outlined
  >
    <v-card-title>
      <v-row
        align="center"
        justify="space-between"
        class="w-100"
      >
        <span>Amostras Registradas</span>
        <div>
          <v-btn
            color="primary"
            @click="openAddModal"
          >
            <v-icon left>mdi-plus</v-icon> Adicionar
          </v-btn>
          <v-btn
            color="secondary"
            @click="downloadReportHandler"
          >
            <v-icon left>mdi-download</v-icon> Baixar Relatório
          </v-btn>
        </div>
      </v-row>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="samples"
      class="elevation-1"
      dense
    >
      <template #item.index="{ index }">
        {{ index + 1 }}
      </template>
      <template #item.actions="{ item }">
        <v-btn
          icon
          color="primary"
          @click="openEditModal(item)"
        >
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
        <v-btn
          icon
          color="error"
          @click="openDeleteModal(item)"
        >
          <v-icon>mdi-delete</v-icon>
        </v-btn>
      </template>
    </v-data-table>

    <!-- Modal de Adicionar/Editar -->
    <v-dialog
      v-model="formDialog"
      max-width="600"
    >
      <v-card>
        <v-card-title class="text-h6">
          {{ isEditing ? "Editar Amostra" : "Adicionar Amostra" }}
        </v-card-title>
        <v-card-text>
          <v-form
            ref="form"
            v-model="formValid"
          >
            <v-text-field
              v-model="formData.ph"
              label="pH"
              type="number"
              :rules="[rules.required]"
              required
            ></v-text-field>
            <v-text-field
              v-model="formData.nitrogen"
              label="Nitrogênio (ppm)"
              type="number"
              :rules="[rules.required]"
              required
            ></v-text-field>
            <v-text-field
              v-model="formData.phosphorus"
              label="Fósforo (ppm)"
              type="number"
              :rules="[rules.required]"
              required
            ></v-text-field>
            <v-text-field
              v-model="formData.potassium"
              label="Potássio (ppm)"
              type="number"
              :rules="[rules.required]"
              required
            ></v-text-field>
            <v-text-field
              v-model="formData.compaction"
              label="Compactação (g/cm³)"
              type="number"
              :rules="[rules.required]"
              required
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            text
            @click="closeFormModal"
            >Cancelar</v-btn
          >
          <v-btn
            color="primary"
            text
            :disabled="!formValid"
            @click="submitForm"
          >
            {{ isEditing ? "Salvar Alterações" : "Adicionar" }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Modal de Confirmação -->
    <v-dialog
      v-model="deleteDialog"
      max-width="400"
    >
      <v-card>
        <v-card-title class="text-h6">Confirmar Exclusão</v-card-title>
        <v-card-text> Tem certeza de que deseja excluir esta amostra? </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            text
            @click="closeDeleteModal"
            >Cancelar</v-btn
          >
          <v-btn
            color="error"
            text
            @click="confirmDelete"
            >Excluir</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script setup>
import { ref } from "vue";
import { downloadReport } from "@/service/sampleService";

defineProps({
  samples: {
    type: Array,
    required: true,
  },
});

const emit = defineEmits(["edit", "delete", "add", "reload"]);

const headers = [
  { title: "ID", value: "id", align: "start", sortable: true },
  { title: "pH", value: "ph", sortable: true },
  { title: "Nitrogênio (ppm)", value: "nitrogen", sortable: true },
  { title: "Fósforo (ppm)", value: "phosphorus", sortable: true },
  { title: "Potássio (ppm)", value: "potassium", sortable: true },
  { title: "Compactação (g/cm³)", value: "compaction", sortable: true },
  { title: "Ações", value: "actions", align: "end", sortable: false },
];

const formDialog = ref(false);
const deleteDialog = ref(false);
const isEditing = ref(false);
const formValid = ref(false);
const selectedSampleId = ref(null);
const formData = ref({
  ph: "",
  nitrogen: "",
  phosphorus: "",
  potassium: "",
  compaction: "",
});

const rules = {
  required: (value) => !!value || "Campo obrigatório.",
  minValue: (min) => (value) => value >= min || `O valor deve ser maior ou igual a ${min}.`,
  maxValue: (max) => (value) => value <= max || `O valor deve ser menor ou igual a ${max}.`,
};

function openAddModal() {
  isEditing.value = false;
  formData.value = {
    ph: "",
    nitrogen: "",
    phosphorus: "",
    potassium: "",
    compaction: "",
  };
  formDialog.value = true;
}

function openEditModal(item) {
  isEditing.value = true;
  selectedSampleId.value = item.id;
  formData.value = { ...item };
  formDialog.value = true;
}

function closeFormModal() {
  formDialog.value = false;
}

function submitForm() {
  if (isEditing.value) {
    emit("edit", { id: selectedSampleId.value, ...formData.value });
  } else {
    emit("add", formData.value);
  }
  closeFormModal();
}

function openDeleteModal(item) {
  selectedSampleId.value = item.id;
  deleteDialog.value = true;
}

function closeDeleteModal() {
  deleteDialog.value = false;
  selectedSampleId.value = null;
}

function confirmDelete() {
  emit("delete", selectedSampleId.value);
  emit("reload");
  closeDeleteModal();
}

function downloadReportHandler() {
  downloadReport();
}
</script>
