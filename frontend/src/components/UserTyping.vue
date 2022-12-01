<template>
    <div class="is-small notification">
        {{user.first_name}} {{user.last_name}} <span class="typing">is typing</span> 
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'UserTyping',
    props: {
        user: {
            type: Object,
            required: true,
            default: () => ({ 
                id: "", 
                username: "", 
                first_name: "",
                last_name: "",
                profile: {},  
            }),
        }
    },
});
</script>

<!-- thanks to https://stackoverflow.com/questions/13014808/is-there-any-way-to-animate-an-ellipsis-with-css-animations-->
<style lang="scss">
.typing:after {
  overflow: hidden;
  display: inline-block;
  vertical-align: bottom;
  -webkit-animation: ellipsis steps(14, end) 1500ms infinite;
  animation: ellipsis steps(14, end) 1500ms infinite;
  content: "\2026";
  /* ascii code for the ellipsis character */
  width: 0px;
}

@keyframes ellipsis {
  to {
    width: 40px;
  }
}

@-webkit-keyframes ellipsis {
  to {
    width: 40px;
  }
}
</style>