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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=201ms, nekobox=230ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-66MS` (url=207ms, nekobox=233ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-74MS` (url=203ms, nekobox=227ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-76MS` (url=198ms, nekobox=250ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-80MS` (url=208ms, nekobox=231ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-79MS` (url=209ms, nekobox=257ms, status=yes)
7. `AKUN-007-HETZNER-VLESS-WS-93MS` (url=210ms, nekobox=239ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-93MS` (url=227ms, nekobox=248ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-67MS` (url=209ms, nekobox=235ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-83MS` (url=211ms, nekobox=257ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-85MS` (url=204ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-103MS` (url=219ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-76MS` (url=225ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-90MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-HETZNER-VLESS-WS-123MS` (url=229ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-128MS` (url=231ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-81MS` (url=250ms, status=HTTP 204)
18. `AKUN-018-NETVIGATOR-VLESS-WS-99MS` (url=199ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-97MS` (url=317ms, status=HTTP 204)
20. `AKUN-020-ZOOM-VLESS-WS-108MS` (url=216ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-142MS` (url=218ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-118MS` (url=224ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-240MS` (url=507ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-240MS` (url=977ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-246MS` (url=489ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
