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
1. `AKUN-001-UNKNOWN-VLESS-WS-65MS` (url=222ms, nekobox=249ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-95MS` (url=219ms, nekobox=252ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=200ms, nekobox=181ms, status=no)
4. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-65MS`
5. `AKUN-004-MEDIUM-VLESS-WS-80MS`
6. `AKUN-005-ZVC-VLESS-WS-75MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-81MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS`
9. `AKUN-008-COMPREND-NET-VLESS-WS-96MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS`
11. `AKUN-011-NODEJS-VLESS-WS-83MS` (url=207ms, nekobox=179ms, status=no)
12. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-79MS` (url=243ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-76MS` (url=204ms, status=HTTP 204)
15. `AKUN-015-CLOUDWEBMANAGE-EU-FR-VLESS-WS-91MS` (url=218ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-73MS` (url=229ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-81MS` (url=209ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-84MS` (url=230ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-90MS` (url=215ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-84MS` (url=196ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-112MS` (url=258ms, status=HTTP 204)
22. `AKUN-022-US-VLESS-WS-81MS` (url=199ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-90MS` (url=200ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-346MS` (url=715ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-400MS` (url=810ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
