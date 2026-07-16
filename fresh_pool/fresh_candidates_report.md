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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-81MS` (url=224ms, nekobox=247ms, status=yes)
2. `AKUN-002-DIXONS-VLESS-WS-84MS` (url=230ms, nekobox=232ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-79MS` (url=220ms, nekobox=247ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-89MS` (url=224ms, nekobox=252ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-90MS` (url=212ms, nekobox=260ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-89MS` (url=232ms, nekobox=228ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-108MS` (url=365ms, nekobox=247ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-109MS` (url=227ms, nekobox=258ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS` (url=269ms, nekobox=253ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-93MS` (url=212ms, nekobox=241ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-123MS` (url=201ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-123MS` (url=233ms, status=HTTP 204)
13. `AKUN-013-WPENG-VLESS-WS-89MS` (url=246ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-85MS` (url=232ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-85MS` (url=229ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-138MS` (url=236ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-138MS` (url=222ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-147MS` (url=226ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-84MS` (url=209ms, status=HTTP 204)
20. `AKUN-020-SPEEDTEST-VLESS-WS-169MS` (url=234ms, status=HTTP 204)
21. `AKUN-021-RS-RAPIDSEEDBOX-20190717-VLESS-WS-242MS` (url=498ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-251MS` (url=543ms, status=HTTP 204)
23. `AKUN-023-UK-GB-DCL-01-20191003-VLESS-WS-249MS` (url=573ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-113MS` (url=209ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-262MS` (url=546ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
