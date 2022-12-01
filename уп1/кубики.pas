var a,b,i,s1,s2,s3:integer;
begin
  read (a,b);
  s1:=0;
  s2:=0;
  s3:=0;
  for i:=1 to 6 do
    begin
    if abs(a-i)<abs(b-i) then
      begin
      s1:=s1+1;
      end;
    if abs(a-i)>abs(b-i) then
     begin
     s2:=s2+1;
     end;
    if abs(a-i)=abs(b-i) then
      begin
      s3:=s3+1;
      end;
     end;
   write (s1,' ',s3,' ',s2);
   end.