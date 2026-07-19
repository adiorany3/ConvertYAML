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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-58MS` (url=215ms, nekobox=251ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS` (url=219ms, nekobox=251ms, status=yes)
3. `AKUN-003-BGP48-HK-VLESS-WS-62MS` (url=226ms, nekobox=256ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-70MS` (url=234ms, nekobox=249ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-72MS` (url=231ms, nekobox=253ms, status=yes)
6. `AKUN-006-RTCOMM-SRAVNI-RU-VLESS-WS-64MS` (url=226ms, nekobox=236ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-84MS` (url=231ms, nekobox=241ms, status=yes)
8. `AKUN-008-CF-CLIENTS-VLESS-WS-66MS` (url=234ms, nekobox=255ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-92MS` (url=214ms, nekobox=263ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-80MS` (url=234ms, nekobox=288ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-83MS` (url=214ms, status=HTTP 204)
12. `AKUN-012-DEV-VLESS-WS-78MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-DEV-VLESS-WS-93MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-62MS` (url=244ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-107MS` (url=222ms, status=HTTP 204)
16. `AKUN-016-ZOOM-VLESS-WS-69MS` (url=236ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-73MS` (url=266ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-104MS` (url=255ms, status=HTTP 204)
19. `AKUN-019-WEBEX-VLESS-WS-115MS` (url=252ms, status=HTTP 204)
20. `AKUN-020-NEXUSMODS-VLESS-WS-122MS` (url=228ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-124MS` (url=212ms, status=HTTP 204)
22. `AKUN-022-CCWU-VLESS-WS-126MS` (url=219ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-97MS` (url=238ms, status=HTTP 204)
24. `AKUN-024-DEV-VLESS-WS-73MS` (url=243ms, status=HTTP 204)
25. `AKUN-025-DEV-VLESS-WS-116MS` (url=204ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
