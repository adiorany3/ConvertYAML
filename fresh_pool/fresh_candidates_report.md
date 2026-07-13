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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-89MS` (url=251ms, nekobox=244ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-119MS` (url=247ms, nekobox=282ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-103MS` (url=209ms, nekobox=218ms, status=no)
4. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-89MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-130MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-122MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-141MS`
8. `AKUN-007-OVH-VLESS-WS-146MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-143MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-124MS` (url=242ms, nekobox=7177ms, status=no)
11. `AKUN-009-ORG-VLESS-WS-140MS`
12. `AKUN-010-UNKNOWN-VLESS-WS-102MS`
13. `AKUN-013-SPEEDTEST-VLESS-WS-141MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-121MS` (url=283ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-122MS` (url=232ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-121MS` (url=218ms, status=HTTP 204)
17. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-200MS` (url=364ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-114MS` (url=209ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-379MS` (url=794ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-380MS` (url=837ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-384MS` (url=878ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-417MS` (url=3830ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-408MS` (url=862ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-441MS` (url=685ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-609MS` (url=585ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
