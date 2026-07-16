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
1. `AKUN-001-UNKNOWN-VLESS-WS-87MS` (url=211ms, nekobox=233ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-88MS` (url=213ms, nekobox=231ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS` (url=220ms, nekobox=241ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-107MS` (url=215ms, nekobox=343ms, status=yes)
5. `AKUN-005-DEV-VLESS-WS-108MS` (url=238ms, nekobox=282ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-112MS` (url=206ms, nekobox=260ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-91MS` (url=228ms, nekobox=244ms, status=yes)
8. `AKUN-008-WEBEX-VLESS-WS-133MS` (url=230ms, nekobox=277ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-126MS` (url=220ms, nekobox=262ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-141MS` (url=221ms, nekobox=250ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-124MS` (url=210ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-113MS` (url=255ms, status=HTTP 204)
13. `AKUN-013-DEV-VLESS-WS-152MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-124MS` (url=231ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-127MS` (url=257ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-173MS` (url=289ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-172MS` (url=262ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-109MS` (url=245ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-104MS` (url=280ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-123MS` (url=235ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-114MS` (url=247ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-121MS` (url=223ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-120MS` (url=249ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-141MS` (url=275ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-165MS` (url=365ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
