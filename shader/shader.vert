#version 130

in vec4 p3d_Vertex;
uniform mat4 p3d_ModelViewProjectionMatrix;

in vec4 color;
out vec4 vert_color;

in float time;


out vec2 texCoord;

void main()  {
  gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
  vert_color = color;
  texCoord = (vec2(gl_Position.x, gl_Position.y) + vec2(1.0)) / vec2(2.0);
}


