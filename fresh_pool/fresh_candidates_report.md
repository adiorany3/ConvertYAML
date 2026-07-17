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
1. `AKUN-001-NEXUSMODS-VLESS-WS-62MS` (url=215ms, nekobox=246ms, status=yes)
2. `AKUN-002-DEV-VLESS-WS-70MS` (url=228ms, nekobox=249ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS` (url=225ms, nekobox=255ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=225ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-82MS` (url=209ms, nekobox=246ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-100MS` (url=304ms, nekobox=324ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-74MS` (url=234ms, nekobox=262ms, status=yes)
8. `AKUN-008-DEV-VLESS-WS-78MS` (url=220ms, nekobox=250ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-92MS` (url=217ms, nekobox=7176ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-101MS`
11. `AKUN-010-WPENG-VLESS-WS-111MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-91MS` (url=219ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-97MS` (url=221ms, status=HTTP 204)
14. `AKUN-014-UK-GB-DCL-01-20191003-VLESS-WS-110MS` (url=231ms, status=HTTP 204)
15. `AKUN-015-UK-GB-DCL-01-20191003-VLESS-WS-115MS` (url=264ms, status=HTTP 204)
16. `AKUN-016-DIXONS-VLESS-WS-70MS` (url=227ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-77MS` (url=217ms, status=HTTP 204)
18. `AKUN-018-NEXUSMODS-VLESS-WS-116MS` (url=220ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-72MS` (url=201ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-87MS` (url=226ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-130MS` (url=252ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-83MS` (url=221ms, status=HTTP 204)
23. `AKUN-023-POLICE-VLESS-WS-108MS` (url=212ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-144MS` (url=222ms, status=HTTP 204)
25. `AKUN-025-1PASSWORD-VLESS-WS-87MS` (url=200ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
