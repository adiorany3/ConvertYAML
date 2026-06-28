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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-101MS` (url=241ms, nekobox=262ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-100MS` (url=245ms, nekobox=358ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-104MS` (url=231ms, nekobox=270ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-109MS` (url=241ms, nekobox=276ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-123MS` (url=237ms, nekobox=252ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-130MS` (url=245ms, nekobox=247ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-120MS` (url=243ms, nekobox=252ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-147MS` (url=266ms, nekobox=298ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-143MS` (url=235ms, nekobox=258ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-122MS` (url=235ms, nekobox=303ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-136MS` (url=242ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-125MS` (url=239ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-158MS` (url=241ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-131MS` (url=246ms, status=HTTP 204)
15. `AKUN-015-UK-GB-DCL-01-20191003-VLESS-WS-177MS` (url=267ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-143MS` (url=245ms, status=HTTP 204)
17. `AKUN-017-COMPREND-NET-VLESS-WS-179MS` (url=223ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-202MS` (url=259ms, status=HTTP 204)
19. `AKUN-019-COMPREND-NET-VLESS-WS-122MS` (url=241ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-168MS` (url=237ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-271MS` (url=474ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-334MS` (url=640ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-328MS` (url=653ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-360MS` (url=709ms, status=HTTP 204)
25. `AKUN-026-RS-RAPIDSEEDBOX-20190717-VLESS-WS-365MS` (url=737ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
