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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS` (url=287ms, nekobox=314ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-105MS` (url=252ms, nekobox=337ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-99MS` (url=255ms, nekobox=328ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-120MS` (url=272ms, nekobox=213ms, status=no)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-118MS` (url=292ms, nekobox=220ms, status=no)
6. `AKUN-004-CLOUDFLARE-VLESS-WS-121MS`
7. `AKUN-005-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-120MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-129MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-126MS` (url=282ms, nekobox=212ms, status=no)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-108MS` (url=264ms, nekobox=213ms, status=no)
11. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-122MS`
12. `AKUN-008-CLOUDFLARE-VLESS-WS-111MS`
13. `AKUN-009-OPENAI-VLESS-WS-149MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-217MS` (url=572ms, nekobox=427ms, status=no)
15. `AKUN-010-CLOUDFLARE-VLESS-WS-337MS`
16. `AKUN-016-MICROSOFT-VLESS-WS-318MS` (url=679ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-350MS` (url=714ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-332MS` (url=664ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-340MS` (url=2644ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-344MS` (url=667ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-332MS` (url=2345ms, status=HTTP 204)
22. `AKUN-023-IRATOM-VLESS-WS-433MS` (url=692ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-581MS` (url=981ms, status=HTTP 204)
24. `AKUN-028-UNKNOWN-VLESS-WS-381MS` (url=824ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-626MS` (url=954ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
