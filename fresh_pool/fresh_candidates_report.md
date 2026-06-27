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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-106MS` (url=244ms, nekobox=222ms, status=no)
2. `AKUN-001-NEXUSMODS-VLESS-WS-113MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-108MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-114MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-119MS`
6. `AKUN-005-DIGITALOCEAN-VLESS-WS-131MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-126MS`
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-133MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-116MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-128MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-116MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-131MS` (url=264ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-127MS` (url=250ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-146MS` (url=268ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-170MS` (url=281ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-157MS` (url=294ms, status=HTTP 204)
17. `AKUN-017-DIGITALOCEAN-VLESS-WS-140MS` (url=268ms, status=HTTP 204)
18. `AKUN-018-CLOUDWEBMANAGE-EU-FR-VLESS-WS-150MS` (url=285ms, status=HTTP 204)
19. `AKUN-019-VULTR-VLESS-WS-135MS` (url=263ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-190MS` (url=331ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-142MS` (url=296ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-296MS` (url=641ms, status=HTTP 204)
23. `AKUN-023-DEV-VLESS-WS-281MS` (url=544ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-336MS` (url=743ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-357MS` (url=650ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
