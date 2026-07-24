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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-94MS` (url=205ms, nekobox=240ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-88MS` (url=230ms, nekobox=243ms, status=yes)
3. `AKUN-003-ES-FORNEX-20160629-VLESS-WS-102MS` (url=242ms, nekobox=253ms, status=yes)
4. `AKUN-004-DIGITALOCEAN-VLESS-WS-94MS` (url=233ms, nekobox=276ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-92MS` (url=236ms, nekobox=242ms, status=yes)
6. `AKUN-006-MEDIUM-VLESS-WS-112MS` (url=228ms, nekobox=255ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-96MS` (url=206ms, nekobox=263ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-104MS` (url=234ms, nekobox=246ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-115MS` (url=222ms, nekobox=249ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-124MS` (url=232ms, nekobox=217ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-113MS`
12. `AKUN-012-MYBB-VLESS-WS-125MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-107MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-119MS` (url=223ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-109MS` (url=234ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-114MS` (url=234ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-122MS` (url=227ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-99MS` (url=242ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-97MS` (url=229ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-108MS` (url=237ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-369MS` (url=786ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-360MS` (url=766ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-359MS` (url=765ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-106MS` (url=728ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-495MS` (url=779ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
