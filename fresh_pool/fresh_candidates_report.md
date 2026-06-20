# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDFLARE-VLESS-WS-68MS` (url=207ms, nekobox=228ms, status=yes)
2. `AKUN-002-MYBB-VLESS-WS-67MS` (url=253ms, nekobox=250ms, status=yes)
3. `AKUN-003-ORACLE-VLESS-WS-75MS` (url=220ms, nekobox=262ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS` (url=250ms, nekobox=192ms, status=no)
5. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-92MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-89MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-87MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-82MS`
11. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-95MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-117MS` (url=252ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-80MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-OPENAI-VLESS-WS-85MS` (url=231ms, status=HTTP 204)
15. `AKUN-015-008500-VLESS-WS-80MS` (url=207ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-86MS` (url=258ms, status=HTTP 204)
17. `AKUN-017-US-VLESS-WS-113MS` (url=340ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-76MS` (url=279ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-401MS` (url=2431ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-94MS` (url=246ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-430MS` (url=794ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-350MS` (url=797ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-396MS` (url=856ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-388MS` (url=837ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-405MS` (url=789ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
