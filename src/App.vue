<template>
  <div class="w-screen h-screen flex items-center py-48">
    <div class="flex flex-col justify-between w-1/4 h-64 min-h-full mx-16 p-4 ">
      <div class="overflow-y-auto w-full mb-4">
        <div
          v-for="message in messages"
          :key="message.time"
          class="flex"
          v-bind:class="{
            'flex-row-reverse': message.re,
          }"
        >
          <p
            class="text-white px-4 py-2  bg-blue-900 shadow-lg "
            v-bind:class="{
              'rounded-full rounded-tr-none self-end': message.re,
              'rounded-full rounded-tl-none ': !message.re,
            }"
          >
            {{ message.text }}
          </p>
          <div class="w-full h-full"></div>
        </div>
      </div>
      <div class="self-end w-full flex justify-between space-x-2">
        <input
          v-model="activeMessage"
          placeholder="Send message"
          type="text"
          class="bg-gray-900 w-full shadow-lg rounded-full px-4 py-2 text-white"
        />
        <button
          @click="sendMessage"
          class="bg-red-500 px-4 py-2 rounded-full font-bold text-white shadow-lg outline-none appearance-none"
        >
          Send
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      activeMessage: "",
      messages: [],
    };
  },
  methods: {
    sendMessage() {
      let remainder = false;
      if (this.messages.length % 2 == 1) {
        remainder = true;
      }
      if (this.activeMessage) {
        this.messages.push({
          user: true,
          text: this.activeMessage,
          time: new Date().toTimeString(),
          re: remainder,
        });
        this.activeMessage = "";
      }
    },
  },
};
</script>
