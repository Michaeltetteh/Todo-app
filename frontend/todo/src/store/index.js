import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todoItem: []
  },
  mutations: {
      UPDATE_TODO_LIST(state, payload) {
        state.todoItem = payload
      }
  },
  actions: {
      getTodoItems({ commit }) {
        axios.get('http://localhost:8000/api/show/').then((res) => {
          commit('UPDATE_TODO_LIST', res.data)
        });
      },

      deleteTodoItem({commit},obj) {
        axios.post(`http://localhost:8000/api/delete/${obj.id}/`).then((res) => {
          // console.log(res.data);
          commit('UPDATE_TODO_LIST',res.data)
        });
      }
  },
  getters: {
    todoItems: state => state.todoItem
  }
})
