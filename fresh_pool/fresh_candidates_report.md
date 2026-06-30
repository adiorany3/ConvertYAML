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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-65MS` (url=288ms, nekobox=241ms, status=yes)
2. `AKUN-002-UK-GB-DCL-01-20191003-VLESS-WS-71MS` (url=200ms, nekobox=251ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-60MS` (url=226ms, nekobox=226ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-76MS` (url=214ms, nekobox=237ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-81MS` (url=212ms, nekobox=256ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-75MS` (url=220ms, nekobox=235ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-71MS` (url=240ms, nekobox=261ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-94MS` (url=206ms, nekobox=234ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-77MS` (url=199ms, nekobox=244ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-81MS` (url=221ms, nekobox=243ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-98MS` (url=211ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-109MS` (url=221ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-118MS` (url=197ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-105MS` (url=199ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-109MS` (url=221ms, status=HTTP 204)
16. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS` (url=220ms, status=HTTP 204)
17. `AKUN-017-COMPREND-NET-VLESS-WS-119MS` (url=206ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-233MS` (url=636ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-250MS` (url=497ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-276MS` (url=603ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-278MS` (url=624ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-253MS` (url=524ms, status=HTTP 204)
23. `AKUN-026-RS-RAPIDSEEDBOX-20190717-VLESS-WS-272MS` (url=605ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-289MS` (url=582ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-389MS` (url=675ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
