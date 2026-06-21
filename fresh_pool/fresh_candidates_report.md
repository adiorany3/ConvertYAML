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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS` (url=222ms, nekobox=238ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=230ms, nekobox=250ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-65MS` (url=213ms, nekobox=248ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS` (url=287ms, nekobox=257ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-91MS` (url=258ms, nekobox=254ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-91MS` (url=217ms, nekobox=302ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-82MS` (url=228ms, nekobox=244ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-102MS` (url=243ms, nekobox=248ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-106MS` (url=261ms, nekobox=256ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-94MS` (url=232ms, nekobox=248ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-97MS` (url=233ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-110MS` (url=243ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-98MS` (url=251ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-112MS` (url=237ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-109MS` (url=236ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-120MS` (url=235ms, status=HTTP 204)
17. `AKUN-017-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-111MS` (url=218ms, status=HTTP 204)
18. `AKUN-018-OPENAI-VLESS-WS-85MS` (url=209ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-167MS` (url=266ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-341MS` (url=741ms, status=HTTP 204)
21. `AKUN-021-CONFLU-VLESS-WS-344MS` (url=733ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-390MS` (url=832ms, status=HTTP 204)
23. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-239MS` (url=826ms, status=HTTP 204)
24. `AKUN-024-SPEEDTEST-VLESS-WS-401MS` (url=827ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-401MS` (url=868ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
