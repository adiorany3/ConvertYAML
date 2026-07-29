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
1. `AKUN-001-UNKNOWN-VLESS-WS-88MS` (url=327ms, nekobox=290ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-102MS` (url=254ms, nekobox=362ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-98MS` (url=337ms, nekobox=299ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-109MS` (url=333ms, nekobox=383ms, status=yes)
5. `AKUN-005-EU-VLESS-WS-112MS` (url=353ms, nekobox=363ms, status=yes)
6. `AKUN-006-MEDIUM-VLESS-WS-96MS` (url=267ms, nekobox=417ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-133MS` (url=321ms, nekobox=299ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-89MS` (url=300ms, nekobox=372ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-102MS` (url=298ms, nekobox=199ms, status=no)
10. `AKUN-009-UNKNOWN-VLESS-WS-124MS`
11. `AKUN-010-DEV-VLESS-WS-103MS`
12. `AKUN-012-008500-VLESS-WS-103MS` (url=262ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-84MS` (url=324ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-114MS` (url=325ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-178MS` (url=354ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-181MS` (url=253ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-185MS` (url=223ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-149MS` (url=335ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-133MS` (url=272ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-118MS` (url=356ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-146MS` (url=333ms, status=HTTP 204)
22. `AKUN-022-HOSTINGER-VLESS-WS-155MS` (url=288ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-104MS` (url=282ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-234MS` (url=400ms, status=HTTP 204)
25. `AKUN-026-CONFLU-VLESS-WS-300MS` (url=632ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
