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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-UNKNOWN-VLESS-WS-79MS` (url=209ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-73MS` (url=228ms, nekobox=256ms, status=yes)
3. `AKUN-003-CHATGPT-VLESS-WS-75MS` (url=217ms, nekobox=248ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS` (url=213ms, nekobox=259ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-84MS` (url=220ms, nekobox=240ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-104MS` (url=212ms, nekobox=252ms, status=yes)
7. `AKUN-007-DEV-VLESS-WS-84MS` (url=214ms, nekobox=246ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-124MS` (url=221ms, nekobox=243ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-114MS` (url=236ms, nekobox=188ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-132MS`
11. `AKUN-010-FASTVPSUS-IPV4-VLESS-WS-157MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-151MS` (url=349ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-201MS` (url=238ms, status=HTTP 204)
14. `AKUN-017-UNKNOWN-VLESS-WS-371MS` (url=785ms, status=HTTP 204)
15. `AKUN-018-UNKNOWN-VLESS-WS-367MS` (url=762ms, status=HTTP 204)
16. `AKUN-019-CLOUDFLARE-VLESS-WS-375MS` (url=732ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-416MS` (url=663ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-417MS` (url=744ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-406MS` (url=669ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-415MS` (url=694ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-419MS` (url=742ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-430MS` (url=774ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-431MS` (url=709ms, status=HTTP 204)
24. `AKUN-031-CLOUDFLARE-VLESS-WS-506MS` (url=1217ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-508MS` (url=801ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
