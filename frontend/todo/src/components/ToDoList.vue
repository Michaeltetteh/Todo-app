<template>
    <div>
        <p>ToDO LIST Component</p>
        <ul v-for="obj in todoItems.data" :key="obj">
            <li> {{ obj }} </li>
        </ul>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: "TodoList",
  created () {
    this.$store.dispatch('getTodoItems');
  },
  computed: {
    ...mapGetters([
      'todoItems'
    ])
  }
};
</script>