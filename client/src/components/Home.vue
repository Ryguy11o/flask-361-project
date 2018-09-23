<template>
	<div class="flex">
    <div class="first">
      <h1>Search within a corpus of text from wikipedia</h1>
      <h3>Project By Ryan O'Neill</h3>
      <div class="item">
        <v-text-field prepend-icon="search" @change="onChange"></v-text-field>
      </div>
    </div>
    <div class="search-title" v-if="search">
      <h2>Search Results for "{{search}}"</h2>
    </div>
      <div v-for="a in answers">
        <Answer v-bind:answer="a"></Answer>
      </div>
	</div>
</template>

<script>
import axios from 'axios';
import Answer from './Answer.vue'

export default {
  name: 'Home',
  components: {
    Answer,
  },
  data() {
    return {
      answers: null,
      search: null,
    };
  },
  methods: {
    onChange(txt){
      if(this.search != txt){
        this.answers = null;
      }
      this.search = txt;
      const data = { question: txt};
      const path = 'http://localhost:5000/getAnswers';

      axios.post(path, data)
        .then((res) => {
          this.answers = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
};
</script>
<style>
  body {
    background-color: #E1BEE7;
  }

  #app {
    font-family: 'Roboto', sans-serif;
  }

  h1, h3 {
    color: white;
  }
</style>
<style scoped>
.first {
  padding: 25px 0;
  border-radius: 4px;
  background-color: #7B1FA2;
}
.flex {
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
  padding-left: 5%;
  padding-right: 5%;
  justify-content: center;
  padding-bottom: 10%;
}

.item {
  margin: 2.5% 5% 2.5% 5%;
/*  padding: 0 20px 10px 20px;*/
  padding: 0 10px 0 10px;
  background-color: #FFF;
  border-radius: 4px;
}

.search-title {
  color: black;
  margin: 2% 0 1% 0;
}
</style>
