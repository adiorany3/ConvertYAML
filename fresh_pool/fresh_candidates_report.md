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
1. `AKUN-001-UNKNOWN-VLESS-WS-81MS` (url=225ms, nekobox=265ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS` (url=294ms, nekobox=7177ms, status=no)
3. `AKUN-002-DIXONS-VLESS-WS-84MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-108MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-113MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-115MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-114MS`
8. `AKUN-007-ZVC-VLESS-WS-93MS`
9. `AKUN-008-DEV-VLESS-WS-122MS`
10. `AKUN-009-DIGITALOCEAN-VLESS-WS-139MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-89MS` (url=216ms, nekobox=197ms, status=no)
12. `AKUN-010-POLICE-VLESS-WS-128MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-89MS` (url=230ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-92MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-128MS` (url=224ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-136MS` (url=202ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-103MS` (url=205ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-138MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-PUBLICDOMAINREGISTRY-NET-VLESS-WS-110MS` (url=212ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-110MS` (url=338ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-156MS` (url=209ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-130MS` (url=325ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-159MS` (url=215ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-112MS` (url=215ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-275MS` (url=419ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
