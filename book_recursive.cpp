void bst::disin(node *root) {
    stack<node*> s;
    node* curr = root;

    while (curr != NULL || !s.empty()) {
        while (curr != NULL) {
            s.push(curr);
            curr = curr->L;
        }
        curr = s.top();
        s.pop();
        cout << curr->data << "\t";
        curr = curr->R;
    }
}

void bst::dispre(node *root) {
    if (root == NULL) return;

    stack<node*> s;
    s.push(root);

    while (!s.empty()) {
        node* curr = s.top();
        s.pop();
        cout << curr->data << "\t";

        if (curr->R) s.push(curr->R);  // right pushed first
        if (curr->L) s.push(curr->L);  // left pushed second so it's processed first
    }
}

void bst::dispost(node *root) {
    if (root == NULL) return;

    stack<node*> s1, s2;
    s1.push(root);

    while (!s1.empty()) {
        node* curr = s1.top();
        s1.pop();
        s2.push(curr);

        if (curr->L) s1.push(curr->L);
        if (curr->R) s1.push(curr->R);
    }

    while (!s2.empty()) {
        cout << s2.top()->data << "\t";
        s2.pop();
    }
}
