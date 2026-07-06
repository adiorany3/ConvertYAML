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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-84MS` (url=211ms, nekobox=319ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-88MS` (url=231ms, nekobox=243ms, status=yes)
3. `AKUN-003-WPENG-VLESS-WS-83MS` (url=236ms, nekobox=248ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-93MS` (url=201ms, nekobox=240ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-96MS` (url=231ms, nekobox=233ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS` (url=209ms, nekobox=237ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-105MS` (url=264ms, nekobox=249ms, status=yes)
8. `AKUN-008-CHSL-HEL-VLESS-WS-107MS` (url=293ms, nekobox=340ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-105MS` (url=246ms, nekobox=340ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-121MS` (url=234ms, nekobox=248ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-109MS` (url=279ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-111MS` (url=274ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-123MS` (url=227ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-91MS` (url=214ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-126MS` (url=247ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-142MS` (url=246ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-128MS` (url=205ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-117MS` (url=222ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-103MS` (url=223ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-288MS` (url=603ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-294MS` (url=623ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-300MS` (url=621ms, status=HTTP 204)
23. `AKUN-024-CELESTARA-VLESS-WS-295MS` (url=611ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-444MS` (url=765ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-472MS` (url=773ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
