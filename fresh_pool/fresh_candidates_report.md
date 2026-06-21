# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-66MS` (url=205ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-100MS` (url=231ms, nekobox=248ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-101MS` (url=221ms, nekobox=259ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-105MS` (url=237ms, nekobox=260ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-98MS` (url=225ms, nekobox=238ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-102MS` (url=203ms, nekobox=246ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-104MS` (url=233ms, nekobox=235ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-150MS` (url=218ms, nekobox=259ms, status=yes)
9. `AKUN-009-INTERNETWORKS-45-131-208-VLESS-WS-69MS` (url=236ms, nekobox=248ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-105MS` (url=211ms, nekobox=243ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-117MS` (url=211ms, status=HTTP 204)
12. `AKUN-012-CONFLU-VLESS-WS-398MS` (url=758ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-375MS` (url=886ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-403MS` (url=860ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-382MS` (url=847ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-383MS` (url=857ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-65MS` (url=235ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-352MS` (url=754ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-337MS` (url=753ms, status=HTTP 204)
20. `AKUN-021-DEV-VLESS-WS-594MS` (url=574ms, status=HTTP 204)
21. `AKUN-027-UNKNOWN-VLESS-WS-416MS` (url=528ms, status=HTTP 204)
22. `AKUN-030-CLOUDFLARE-VLESS-WS-825MS` (url=2226ms, status=HTTP 204)
23. `AKUN-034-UNKNOWN-VLESS-WS-786MS` (url=1156ms, status=HTTP 204)
24. `AKUN-035-UNKNOWN-VLESS-WS-772MS` (url=1207ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
