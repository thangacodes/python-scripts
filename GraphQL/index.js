const { ApolloServer } = require('apollo-server');
const gql = require('graphql-tag');

// Define a simple schema
const typeDefs = gql`
  type Query {
    hello: String
    name: String
    age: String
    work: String
    designation: String
  }
`;

// Define resolvers to handle queries
const resolvers = {
  Query: {
    hello: ()       => 'Hello, How are you?',
    name: ()        => 'Hey, Your name is Thangadurai!',
    age: ()         => 'Hey, your age is: 36',
    work: ()        => 'Working at try-devops.xyz',
    designation: () => 'Senior Cloud DevOps Engineer',
  },
};

// Create the ApolloServer instance
const server = new ApolloServer({ typeDefs, resolvers });

// Start the server
server.listen().then(({ url }) => {
  console.log(`Server ready at ${url}`);
});
