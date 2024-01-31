<template>
  <div class="task">
    <div class="text">
      <span>{{ text }}</span>
    </div>
    <div>
      <button class="delete" type="button" @click="deletetask()">
        <img src="../assets/x.svg" draggable="false" />
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      required: true,
    },
  },
  methods: {
    deletetask(){
      this.$emit("deltask")
    }
  }
};
</script>
