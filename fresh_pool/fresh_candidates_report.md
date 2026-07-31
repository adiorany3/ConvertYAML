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
1. `AKUN-001-UNKNOWN-VLESS-WS-60MS` (url=229ms, nekobox=267ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-62MS` (url=224ms, nekobox=250ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-62MS` (url=222ms, nekobox=255ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-62MS` (url=222ms, nekobox=253ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-84MS` (url=235ms, nekobox=260ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=250ms, nekobox=272ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-73MS` (url=231ms, nekobox=256ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-101MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-97MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-105MS`
11. `AKUN-013-CLOUDFLARE-VLESS-WS-105MS` (url=246ms, status=HTTP 204)
12. `AKUN-014-UNKNOWN-VLESS-WS-90MS` (url=259ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-153MS` (url=313ms, status=HTTP 204)
14. `AKUN-016-PAGES-VLESS-WS-137MS` (url=259ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-267MS` (url=2042ms, status=HTTP 204)
16. `AKUN-018-UNKNOWN-VLESS-WS-284MS` (url=724ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-449MS` (url=811ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-426MS` (url=706ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-425MS` (url=706ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-561MS` (url=913ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-582MS` (url=918ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-669MS` (url=1689ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-590MS` (url=1300ms, status=HTTP 204)
24. `AKUN-028-UNKNOWN-VLESS-WS-329MS` (url=3896ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-631MS` (url=3597ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
