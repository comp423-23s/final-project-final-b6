import { Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { User, MemberService } from '../../members/members.service';
import { Organization } from 'src/app/organizations/organizations.service';
@Component({
  selector: 'app-leave-dialog',
  templateUrl: './leave-dialog.component.html',
  styleUrls: ['./leave-dialog.component.css']
})
export class LeaveDialogComponent {
  constructor(private memberService: MemberService,
    private dialogRef: MatDialogRef<LeaveDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: { organizationName: String, user: User }
  ) { }

  ngOnInit(): void { }
  deleteEvent() {
    this.memberService.deleteMember(this.data.organizationName, this.data.user).subscribe(() => {
      this.dialogRef.close();
    });
  }
}