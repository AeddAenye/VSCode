<template>
  <div class="task">
    <div class="text">
      <span>{{ text }}</span>
    </div>
    <div>
      <button class="delete" type="button">
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
};
</script>
