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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=198ms, nekobox=229ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-73MS` (url=215ms, nekobox=265ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=212ms, nekobox=225ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-81MS` (url=230ms, nekobox=241ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-91MS` (url=197ms, nekobox=218ms, status=no)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS` (url=206ms, nekobox=183ms, status=no)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-82MS` (url=209ms, nekobox=184ms, status=no)
8. `AKUN-005-CLOUDFLARE-VLESS-WS-86MS`
9. `AKUN-006-CLOUDFLARE-VLESS-WS-83MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-74MS` (url=204ms, nekobox=188ms, status=no)
11. `AKUN-007-UNKNOWN-VLESS-WS-103MS`
12. `AKUN-008-CLOUDFLARE-VLESS-WS-103MS`
13. `AKUN-009-COMPREND-NET-VLESS-WS-103MS`
14. `AKUN-010-COMPREND-NET-VLESS-WS-85MS`
15. `AKUN-015-DEV-VLESS-WS-83MS` (url=207ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-91MS` (url=208ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-105MS` (url=199ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-123MS` (url=223ms, status=HTTP 204)
19. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-65MS` (url=213ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-104MS` (url=194ms, status=HTTP 204)
21. `AKUN-021-COMPREND-NET-VLESS-WS-155MS` (url=209ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-69MS` (url=218ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-219MS` (url=322ms, status=HTTP 204)
24. `AKUN-024-UK-GB-DCL-01-20191003-VLESS-WS-64MS` (url=198ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-360MS` (url=810ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
