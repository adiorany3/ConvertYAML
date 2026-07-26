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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-86MS` (url=201ms, nekobox=237ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-88MS` (url=200ms, nekobox=265ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-92MS` (url=202ms, nekobox=264ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-93MS` (url=199ms, nekobox=231ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-86MS` (url=231ms, nekobox=228ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-91MS` (url=201ms, nekobox=230ms, status=yes)
7. `AKUN-007-GOOGLE-VLESS-WS-93MS` (url=198ms, nekobox=260ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS` (url=233ms, nekobox=242ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-97MS` (url=217ms, nekobox=243ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-85MS` (url=198ms, nekobox=229ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-104MS` (url=206ms, status=HTTP 204)
12. `AKUN-012-008500-VLESS-WS-108MS` (url=207ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-98MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-94MS` (url=233ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-104MS` (url=206ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-101MS` (url=209ms, status=HTTP 204)
17. `AKUN-017-SKK-VLESS-WS-126MS` (url=248ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-101MS` (url=198ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-113MS` (url=198ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-105MS` (url=207ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-362MS` (url=814ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-362MS` (url=742ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-360MS` (url=4341ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-370MS` (url=4950ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-717MS` (url=1205ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
