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
1. `AKUN-001-OVH-VLESS-WS-66MS` (url=199ms, nekobox=255ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=210ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-65MS` (url=224ms, nekobox=240ms, status=yes)
4. `AKUN-004-WPENG-VLESS-WS-61MS` (url=211ms, nekobox=260ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-77MS` (url=236ms, nekobox=265ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=212ms, nekobox=252ms, status=yes)
7. `AKUN-007-CHSL-HEL-VLESS-WS-97MS` (url=226ms, nekobox=251ms, status=yes)
8. `AKUN-008-VULTR-VLESS-WS-90MS` (url=218ms, nekobox=244ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS` (url=220ms, nekobox=235ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS` (url=225ms, nekobox=227ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-78MS` (url=229ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-97MS` (url=231ms, status=HTTP 204)
13. `AKUN-013-PAGES-VLESS-WS-122MS` (url=209ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-98MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-101MS` (url=261ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-248MS` (url=507ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-236MS` (url=623ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-269MS` (url=598ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-277MS` (url=590ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-271MS` (url=370ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-288MS` (url=656ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-285MS` (url=609ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-247MS` (url=597ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-242MS` (url=533ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-430MS` (url=684ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
