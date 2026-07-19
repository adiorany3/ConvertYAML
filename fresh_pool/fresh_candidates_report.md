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
1. `AKUN-001-RU-BEGET-20090529-VLESS-WS-86MS` (url=231ms, nekobox=236ms, status=yes)
2. `AKUN-002-DIXONS-VLESS-WS-83MS` (url=229ms, nekobox=263ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-91MS` (url=204ms, nekobox=232ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS` (url=224ms, nekobox=235ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-88MS` (url=283ms, nekobox=7177ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-91MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-98MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-105MS`
10. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-104MS`
11. `AKUN-010-466688-VLESS-WS-81MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-116MS` (url=211ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-91MS` (url=204ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-85MS` (url=245ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-95MS` (url=208ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-112MS` (url=253ms, status=HTTP 204)
17. `AKUN-017-WPENG-VLESS-WS-90MS` (url=241ms, status=HTTP 204)
18. `AKUN-018-NFORCE-VLESS-WS-94MS` (url=222ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-142MS` (url=252ms, status=HTTP 204)
20. `AKUN-020-SAVVY-7-VLESS-WS-104MS` (url=253ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-125MS` (url=229ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-119MS` (url=258ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-120MS` (url=219ms, status=HTTP 204)
24. `AKUN-024-ZOOM-VLESS-WS-133MS` (url=199ms, status=HTTP 204)
25. `AKUN-025-MEDIUM-VLESS-WS-94MS` (url=208ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
