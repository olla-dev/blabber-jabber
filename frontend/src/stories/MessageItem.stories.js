import MessageItem from '../components/MessageItem'

// More on default export: https://storybook.js.org/docs/vue/writing-stories/introduction#default-export
export default {
  title: 'Chat/MessageItem',
  component: MessageItem,
  // More on argTypes: https://storybook.js.org/docs/vue/api/argtypes
  argTypes: {
    message: { 
      id: 1, 
      author_id: 1, 
      content: "Hello world", 
      sent_time_utc: new Date()
    },
    user: { 
      first_name: "John", 
      last_name:"Doe",
      profile: { 
        bio: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ornare magna eros, eu pellentesque tortor vestibulum ut. Maecenas non massa sem. Etiam finibus odio quis feugiat facilisis.",
        online: true 
      } 
    },
  },
};

// More on component templates: https://storybook.js.org/docs/vue/writing-stories/introduction#using-args
const Template = (args) => ({
  // Components used in your story `template` are defined in the `components` object
  components: { MessageItem },
  // The story's `args` need to be mapped into the template through the `setup()` method
  setup() {
    return { args };
  },
  // And then the `args` are bound to your component with `v-bind="args"`
  template: '<message-item v-bind="args" />',
});

export const Sent = Template.bind({});
// More on args: https://storybook.js.org/docs/vue/writing-stories/args
Sent.args = {
  message: { 
    id: 1, 
    author_id: 1, 
    content: "Hello world", 
    sent_time_utc: new Date()
  },
  user: { 
    first_name: "John", 
    last_name:"Doe",
    profile: { 
      bio: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ornare magna eros, eu pellentesque tortor vestibulum ut. Maecenas non massa sem. Etiam finibus odio quis feugiat facilisis.",
      online: true 
    } 
  },
};