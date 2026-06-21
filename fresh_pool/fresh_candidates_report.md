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
1. `AKUN-001-008500-VLESS-WS-78MS` (url=210ms, nekobox=237ms, status=yes)
2. `AKUN-002-NETCUP-VLESS-WS-79MS` (url=209ms, nekobox=248ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-89MS` (url=222ms, nekobox=256ms, status=yes)
4. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-90MS` (url=218ms, nekobox=237ms, status=yes)
5. `AKUN-005-VULTR-VLESS-WS-73MS` (url=214ms, nekobox=236ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-81MS` (url=221ms, nekobox=254ms, status=yes)
7. `AKUN-007-CLOUDWEBMANAGE-EU-FR-VLESS-WS-90MS` (url=210ms, nekobox=238ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-87MS` (url=254ms, nekobox=233ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-106MS` (url=197ms, nekobox=257ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-108MS` (url=230ms, nekobox=256ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-109MS` (url=229ms, status=HTTP 204)
12. `AKUN-012-MYBB-VLESS-WS-98MS` (url=217ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-101MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-1PASSWORD-VLESS-WS-79MS` (url=222ms, status=HTTP 204)
15. `AKUN-015-EU-VLESS-WS-134MS` (url=198ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-154MS` (url=195ms, status=HTTP 204)
17. `AKUN-017-OPENAI-VLESS-WS-168MS` (url=261ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-135MS` (url=231ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-181MS` (url=209ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-80MS` (url=219ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-236MS` (url=505ms, status=HTTP 204)
22. `AKUN-022-ADF-VLESS-WS-79MS` (url=225ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-259MS` (url=542ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-252MS` (url=563ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-250MS` (url=562ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
