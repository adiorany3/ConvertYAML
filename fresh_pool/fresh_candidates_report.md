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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-91MS` (url=210ms, nekobox=235ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-95MS` (url=225ms, nekobox=249ms, status=yes)
3. `AKUN-003-008500-VLESS-WS-91MS` (url=205ms, nekobox=241ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-102MS` (url=214ms, nekobox=249ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-101MS` (url=233ms, nekobox=294ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-93MS` (url=220ms, nekobox=246ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-119MS` (url=205ms, nekobox=263ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-100MS` (url=242ms, nekobox=311ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-100MS` (url=228ms, nekobox=233ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-121MS` (url=220ms, nekobox=262ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-112MS` (url=220ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-105MS` (url=249ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-124MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-108MS` (url=235ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-99MS` (url=233ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-97MS` (url=220ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-141MS` (url=205ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-151MS` (url=227ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-223MS` (url=503ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-232MS` (url=512ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-269MS` (url=539ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-267MS` (url=551ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-290MS` (url=602ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-258MS` (url=559ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-294MS` (url=549ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
