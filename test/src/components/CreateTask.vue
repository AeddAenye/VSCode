<template>
        <div class="inputarea">
      <div class="userinput">
        <input type="text" placeholder="Нужно просто начать" />
      </div>
      <div>
        <button type="button" class="addtask">
          <img src="../assets/plus.svg" draggable="false" />
        </button>
      </div>
    </div>
</template>

<script>
import Task from './Task.vue';

export default {
  components: {
    Task,
  },
  data() {
    return {
    };
  },
  methods: {

  },
};
</script>