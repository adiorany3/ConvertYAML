# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
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
1. `AKUN-001-ORACLE-VLESS-WS-70MS` (url=210ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=215ms, nekobox=197ms, status=no)
3. `AKUN-003-DEV-VLESS-WS-77MS` (url=216ms, nekobox=215ms, status=no)
4. `AKUN-002-CLOUDFLARE-VLESS-WS-91MS`
5. `AKUN-003-CLOUDFLARE-VLESS-WS-99MS`
6. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-111MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-113MS` (url=228ms, nekobox=222ms, status=no)
8. `AKUN-005-CLOUDFLARE-VLESS-WS-84MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-94MS` (url=229ms, nekobox=187ms, status=no)
10. `AKUN-006-CLOUDFLARE-VLESS-WS-107MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-92MS` (url=204ms, nekobox=188ms, status=no)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-113MS` (url=205ms, nekobox=189ms, status=no)
13. `AKUN-007-CONFLU-VLESS-WS-228MS`
14. `AKUN-008-CLOUDFLARE-VLESS-WS-256MS`
15. `AKUN-009-WPENG-VLESS-WS-266MS`
16. `AKUN-010-UNKNOWN-VLESS-WS-229MS`
17. `AKUN-017-UNKNOWN-VLESS-WS-265MS` (url=601ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-268MS` (url=559ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-264MS` (url=480ms, status=HTTP 204)
20. `AKUN-025-UNKNOWN-VLESS-WS-467MS` (url=820ms, status=HTTP 204)
21. `AKUN-026-UNKNOWN-VLESS-WS-474MS` (url=661ms, status=HTTP 204)
22. `AKUN-029-UNKNOWN-VLESS-WS-512MS` (url=2083ms, status=HTTP 204)
23. `AKUN-034-UNKNOWN-VLESS-WS-621MS` (url=1397ms, status=HTTP 204)
24. `AKUN-035-UNKNOWN-VLESS-WS-680MS` (url=2069ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
