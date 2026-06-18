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
1. `AKUN-001-GOV-VLESS-WS-122MS` (url=464ms, nekobox=320ms, status=yes)
2. `AKUN-002-DEV-VLESS-WS-113MS` (url=300ms, nekobox=341ms, status=no)
3. `AKUN-003-DEV-VLESS-WS-118MS` (url=411ms, nekobox=215ms, status=no)
4. `AKUN-004-DEV-VLESS-WS-130MS` (url=395ms, nekobox=347ms, status=no)
5. `AKUN-002-UNKNOWN-VLESS-WS-126MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-153MS` (url=395ms, nekobox=223ms, status=no)
7. `AKUN-003-CLOUDFLARE-VLESS-WS-122MS`
8. `AKUN-004-UNKNOWN-VLESS-WS-113MS`
9. `AKUN-005-OPENAI-VLESS-WS-104MS`
10. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-285MS`
11. `AKUN-007-UNKNOWN-VLESS-WS-303MS`
12. `AKUN-008-CLOUDFLARE-VLESS-WS-327MS`
13. `AKUN-009-CLOUDFLARE-VLESS-WS-335MS`
14. `AKUN-017-UNKNOWN-VLESS-WS-339MS` (url=4761ms, nekobox=464ms, status=no)
15. `AKUN-010-CLOUDFLARE-VLESS-WS-547MS`
16. `AKUN-021-UNKNOWN-VLESS-WS-581MS` (url=2630ms, status=HTTP 204)
17. `AKUN-022-CLOUDFLARE-VLESS-WS-640MS` (url=1069ms, status=HTTP 204)
18. `AKUN-023-CHATGPT-VLESS-WS-589MS` (url=1218ms, status=HTTP 204)
19. `AKUN-024-IRATOM-VLESS-WS-504MS` (url=714ms, status=HTTP 204)
20. `AKUN-026-RS-RAPIDSEEDBOX-20190717-VLESS-WS-560MS` (url=1311ms, status=HTTP 204)
21. `AKUN-027-CLOUDFLARE-VLESS-WS-770MS` (url=797ms, status=HTTP 204)
22. `AKUN-028-CLOUDFLARE-VLESS-WS-787MS` (url=1196ms, status=HTTP 204)
23. `AKUN-030-CLOUDFLARE-VLESS-WS-781MS` (url=1368ms, status=HTTP 204)
24. `AKUN-032-UNKNOWN-VLESS-WS-804MS` (url=1164ms, status=HTTP 204)
25. `AKUN-034-CLOUDFLARE-VLESS-WS-801MS` (url=1266ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
