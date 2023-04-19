import { Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { User, MemberService } from '../../members/members.service';

@Component({
  selector: 'app-member-delete-dialog',
  templateUrl: './member-delete-dialog.component.html',
  styleUrls: ['./member-delete-dialog.component.css']
})
export class MemberDeleteDialogComponent {

  constructor(private memberService: MemberService,
    private dialogRef: MatDialogRef<MemberDeleteDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: { organizationName: String, user: User }
  ) { }

  ngOnInit(): void { }
  deleteEvent() {
    this.memberService.deleteMember(this.data.organizationName, this.data.user).subscribe(() => {
      this.dialogRef.close();
    });
  }
}
