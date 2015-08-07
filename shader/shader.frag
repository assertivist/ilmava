#version 130

in vec4 vert_color;
out vec4 frag_color;

uniform sampler2D p3d_Texture0;
in vec2 texCoord;
uniform float osg_FrameTime;

void main () {
  frag_color = vert_color;
  if(mod(osg_FrameTime, 3.0) > 1.6) {
  	frag_color.z = 0.0;
  }
  ivec2 size = textureSize(p3d_Texture0, 0);
  float total = floor(texCoord.x*float(size.x)) + floor(texCoord.y*float(size.y));
  bool is_even = mod(total, 2.0) == 0.0;
  vec4 blk = vec4(0.0,0.0,0.0,0.0);
  frag_color = (is_even) ? blk : vert_color;


  //frag_color.z = 0.0;
}

