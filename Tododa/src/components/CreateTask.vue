<template>
  <div class="inputarea">
    <div class="usertext">
      <input type="text" placeholder="Нужно просто начать" v-model="txt" />
    </div>

    <div class="tag">
      <input type="text" placeholder="Добавьте тэг" v-model="tag" />
    </div>
    <div class="buttons">
      <button type="button" class="addtask" @click="taskcreate">
        <img src="../assets/plus.svg" draggable="false" />
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      txt: '',
      tag: '',
    };
  },
  methods: {
    taskcreate() {
      if (this.txt.trim() !== '') {
        if (this.tag.trim() === '') {
          this.tag = 'Без тэга'
        }
        this.$emit('addtask', { text: this.txt, tag: this.tag })

        this.txt = '';
        this.tag = ''
      }
    },
  },
};
</script>

<style scoped>
.inputarea {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 20px 0px;
  padding: 20px;
  background-color: var(--block-bg);
  border-radius: 15px;
}

.usertext{
  width: 55%;
}

.tag{
  width: 25%;
}


.inputarea input {
  width: 100%;
  font-size: 1.5rem;
  padding: 10px 20px;
  border-radius: 10px;
  border: none;
}

.inputarea button {
  background-color: rgb(126, 187, 240);
}

.inputarea button:hover {
  background-color: rgb(88, 170, 242);
}

.inputarea button:active {
  scale: 0.95;
}
</style>