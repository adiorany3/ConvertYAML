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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-87MS` (url=208ms, nekobox=203ms, status=no)
2. `AKUN-001-UNKNOWN-VLESS-WS-84MS`
3. `AKUN-003-CLOUDFLARE-VLESS-WS-83MS` (url=211ms, nekobox=191ms, status=no)
4. `AKUN-002-UNKNOWN-VLESS-WS-92MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-100MS` (url=200ms, nekobox=211ms, status=no)
6. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-101MS`
7. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-123MS`
8. `AKUN-005-CLOUDFLARE-VLESS-WS-95MS`
9. `AKUN-006-CLOUDFLARE-VLESS-WS-96MS`
10. `AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-129MS`
11. `AKUN-008-CLOUDFLARE-VLESS-WS-121MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-129MS` (url=199ms, nekobox=192ms, status=no)
13. `AKUN-009-CLOUDFLARE-VLESS-WS-92MS`
14. `AKUN-010-US-VLESS-WS-118MS`
15. `AKUN-015-CLOUDFLARE-VLESS-WS-117MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-CLOUDWEBMANAGE-EU-FR-VLESS-WS-113MS` (url=207ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-111MS` (url=225ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-100MS` (url=239ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-242MS` (url=519ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-264MS` (url=554ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-269MS` (url=553ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-285MS` (url=608ms, status=HTTP 204)
23. `AKUN-024-MICROSOFT-VLESS-WS-293MS` (url=563ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-334MS` (url=572ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-275MS` (url=570ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
