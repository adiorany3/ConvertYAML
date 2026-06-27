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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-84MS` (url=224ms, nekobox=253ms, status=yes)
2. `AKUN-002-CNAE-VLESS-WS-84MS` (url=206ms, nekobox=257ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS` (url=228ms, nekobox=228ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-89MS` (url=206ms, nekobox=261ms, status=yes)
5. `AKUN-005-VULTR-VLESS-WS-92MS` (url=221ms, nekobox=254ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-90MS` (url=230ms, nekobox=228ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-101MS` (url=232ms, nekobox=239ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-99MS` (url=224ms, nekobox=252ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-88MS` (url=234ms, nekobox=246ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-109MS` (url=252ms, nekobox=235ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-100MS` (url=202ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-91MS` (url=200ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-83MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-89MS` (url=279ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-77MS` (url=223ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-90MS` (url=226ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-89MS` (url=218ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-120MS` (url=206ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-89MS` (url=230ms, status=HTTP 204)
20. `AKUN-020-COMPREND-NET-VLESS-WS-131MS` (url=199ms, status=HTTP 204)
21. `AKUN-021-US-VLESS-WS-94MS` (url=276ms, status=HTTP 204)
22. `AKUN-022-CONFLU-VLESS-WS-239MS` (url=583ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-250MS` (url=507ms, status=HTTP 204)
24. `AKUN-024-WPENG-VLESS-WS-269MS` (url=565ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-282MS` (url=574ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
