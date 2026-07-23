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
1. `AKUN-001-LEVIKOGJGFDD-VLESS-WS-100MS` (url=228ms, nekobox=281ms, status=yes)
2. `AKUN-002-DEV-VLESS-WS-97MS` (url=215ms, nekobox=252ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-122MS` (url=213ms, nekobox=240ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-104MS` (url=212ms, nekobox=237ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-93MS` (url=209ms, nekobox=236ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-101MS` (url=210ms, nekobox=245ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-112MS` (url=218ms, nekobox=251ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-105MS` (url=222ms, nekobox=245ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-140MS` (url=319ms, nekobox=377ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-120MS` (url=207ms, nekobox=237ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-113MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-130MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-145MS` (url=221ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-115MS` (url=217ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-111MS` (url=211ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-122MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-105MS` (url=220ms, status=HTTP 204)
18. `AKUN-018-LEVIKOGJGFDD-VLESS-WS-133MS` (url=243ms, status=HTTP 204)
19. `AKUN-019-ZVC-VLESS-WS-118MS` (url=206ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-376MS` (url=819ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-377MS` (url=798ms, status=HTTP 204)
22. `AKUN-022-SPEEDTEST-VLESS-WS-380MS` (url=760ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-398MS` (url=747ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-364MS` (url=719ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-722MS` (url=1490ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
